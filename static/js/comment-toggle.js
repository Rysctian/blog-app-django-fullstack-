   // Get references to the button, form, and section
   var commentToggleBtn = document.getElementById('commentToggleBtn');
   var commentForm = document.getElementById('commentForm');
   var commentSection = document.getElementById('commentSection');

   // Initial state: comment form is hidden
   commentForm.style.display = 'none';

   // Toggle function
   function toggleCommentForm() {
      if (commentForm.style.display === 'none') {
         commentForm.style.display = 'block';
      } else {
         commentForm.style.display = 'none';
      }
   }

   // Attach the toggle function to the button click event
   commentToggleBtn.addEventListener('click', toggleCommentForm);