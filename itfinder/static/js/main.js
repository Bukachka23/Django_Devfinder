// Retrieve the search form element by its id
let searchForm = document.getElementById('searchForm')
// Get all elements with class 'page-link'
let pageLinks = document.getElementsByClassName('page-link')

// Check if the search form exists
if (searchForm) {
    // Loop over all the elements with class 'page-link'
    for (let i = 0; pageLinks.length > i; i++) {
        // Add a click event listener to each 'page-link' element
        pageLinks[i].addEventListener('click', function (e) {
            // Prevent the default action of the event (which is navigating to the href of the clicked link)
            e.preventDefault()

            // Retrieve the 'page' data attribute of the clicked link
            let page = this.dataset.page

            // Add a hidden input field with the page number to the search form
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

            // Submit the search form programmatically
            searchForm.submit()
        })
    }
}

// Get all elements with class 'project-tag'
let tags = document.getElementsByClassName('project-tag')

// Loop over all the elements with class 'project-tag'
for (let i = 0; tags.length > i; i++) {
    // Add a click event listener to each 'project-tag' element
    tags[i].addEventListener('click', (e) => {
        // Retrieve the 'tag' and 'project' data attributes of the clicked element
        let tagId = e.target.dataset.tag
        let projectId = e.target.dataset.project

        // Make a DELETE request to the '/api/remove-tag/' endpoint with the project and tag ids as the request body
        fetch('http://127.0.0.1:8000/api/remove-tag/', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'project': projectId, 'tag': tagId })
        })
        // Parse the response as JSON
        .then(response => response.json())
        .then(data => {
            // Remove the clicked element from the DOM
            e.target.remove()
        })
    })
}
