document.addEventListener('DOMContentLoaded', function() {
    const showFormButton = document.getElementById('showFormButton');
    const myForm = document.getElementById('myForm');

    showFormButton.addEventListener('click', function() {
        // Toggle the visibility of the form
        if (myForm.style.display === 'none' || myForm.style.display === '') {
            myForm.style.display = 'block';
        } else {
            myForm.style.display = 'none';
        }
    });
});
