from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView, RedirectView, FormView, View
from .models import Post, Draft, Comment
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse_lazy
from .forms import SignupForm, LoginForm, PostForm, DraftForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class MenuView(TemplateView):
    """
    This class will serve to display the menu page of the application
    """
    template_name = "menu.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(is_published=True).order_by('-created_on')
        context['posts'] = posts
        return context


class CreatePostView(CreateView):
    """
    This class will serve users to create new posts
    """
    template_name = "post.html"
    form_class = PostForm
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        if self.request.POST.get('submit_type') == 'draft':
            # Save as draft
            draft_form = DraftForm(self.request.POST, self.request.FILES)  # Use DraftForm for draft
            if draft_form.is_valid():
                draft = draft_form.save(commit=False)
                draft.user = self.request.user
                draft.save()
                messages.success(self.request, message="Draft saved successfully")
                return redirect(reverse_lazy("profile"))
            else:
                messages.error(self.request, message="Invalid draft form data")
                return self.form_invalid(form)
        else:
            post = form.save(commit=False)
            post.user = self.request.user
            post.save()
            messages.success(self.request, message="Post created successfully")
            return super().form_valid(form)

    def form_invalid(self, form):
        """
        This function is called when the user submits the form with invalid data
        """
        messages.error(self.request, message="You need to attribute a title picture and content")
        return super().form_invalid(form)


class LogoutView(RedirectView):
    """
    This class serves to users logout of the blog and redirect to the menu page
    """
    url = reverse_lazy('menu')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class LoginView(FormView):
    """
    This class serves to manage the login page
    """
    template_name = "login"
    form_class = LoginForm
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        """
        This function is called when the user does the login correctly and generate a message case not
        """
        # Authenticate the user using the form data
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            messages.success(self.request, "Login successful")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid username or password")
            return self.form_invalid(form)


class SignUpView(FormView):
    """
    This class serves to manage the signup page saving the user if is correct and generating an error message if not
    """
    template_name = "signup.html"
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """
        This function is called when the user do the login correctly
        """

        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        User.objects.create_user(username=username, email=email, password=password, is_active=True)

        messages.success(self.request, message="Login successful")
        login(self.request, form.get_user())
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        This function is called when the user do the login incorrectly
        """
        messages.error(self.request, message="Invalid information")
        return super().form_invalid(form)


class ProfileView(TemplateView):
    """
    This class will serve to display the posts and drafts from users, also to update and delete them
    """
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        """
        This method it's to display the posts from users
        """
        context = super().get_context_data(**kwargs)
        # Filter posts by the logged-in user
        user_posts = Post.objects.filter(user=self.request.user).order_by('-created_on')
        context['user_posts'] = user_posts
        return context


class UpdatePostView(UpdateView):
    """
    This class will serve users to update information in their posts
    """
    template_name = "update_post.html"
    model = Post
    fields = ['image', 'title', 'content']
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        return super().form_valid(form)


class DeletePostView(DeleteView):
    """
    This class will serve to delete posts and redirect users to the menu
    """
    model = Post
    success_url = reverse_lazy("menu")


class DraftsView(TemplateView):
    """
    This class will serve to display draft posts
    """
    template_name = "drafts.html"
    model = Draft

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        drafts = Draft.objects.all().order_by('-created_on')
        context['drafts'] = drafts
        return context


class UpdateDraftView(UpdateView):
    """
    This class serves to update drafts
    """
    template_name = "update_draft.html"
    model = DraftForm
    fields = ['title', 'image', 'content']
    success_url = reverse_lazy('drafts')

    def form_valid(self, form):
        if 'post_draft' in self.request.POST:
            # Save the draft as a post
            post = form.save(commit=False)
            post.user = self.request.user
            post.save()
            self.object.delete()
            return redirect('menu')
        else:
            return super().form_valid(form)


class DeleteDraftView(DeleteView):
    model = Draft
    success_url = reverse_lazy("drafts")


class AddCommentView(View):
    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        body = request.POST.get('body')
        comment = Comment.objects.create(post=post, user=request.user, body=body)
        return redirect('menu')


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'edit_comment.html'
    fields = ['body']
    success_url = '/'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'confirm_delete_comment.html'
    success_url = reverse_lazy('menu')
