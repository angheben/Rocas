window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        // Fetch more posts
        fetchMorePosts();
    }
});