alert("Welcome to Deglobeal profile page more mortifications are yet to come, feel free to send me an email")

document.addEventListener('DOMContentLoaded', () => {
    const verticalNav = document.querySelector('.navi_bar_vertical');
    
    // Toggle nav on click
    verticalNav.addEventListener('click', (e) => {
        e.stopPropagation();
        verticalNav.classList.toggle('active');
    });

    // Close nav when clicking outside
    document.addEventListener('click', (e) => {
        if (!verticalNav.contains(e.target)) {
            verticalNav.classList.remove('active');
        }
    });

    // Optional: Close nav when clicking links
    const navLinks = document.querySelectorAll('.navi_bar_vertical a');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            verticalNav.classList.remove('active');
        });
    });
});


// login form 

document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();  // Prevent form submission

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch('/api/user/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}',  // Add CSRF token for security
        },
        body: JSON.stringify({
            email: email,
            password: password,
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Login successful") {
            window.location.href = "/";  // Redirect to home page
        } else {
            alert("Login failed. Please check your credentials.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
