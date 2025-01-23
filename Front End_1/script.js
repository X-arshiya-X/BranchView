document.getElementById("bst-form").addEventListener("submit", function(event) {
    event.preventDefault();

    // Get form values
    const treeType = document.getElementById("tree-type").value;
    const values = document.getElementById("values").value.split(',').map(Number);

    // Call the backend to create the tree
    fetch("/create_bst", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            tree_type: treeType,
            values: values
        })
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response (e.g., show the tree)
        visualizeTree(data);
    })
    .catch(error => {
        console.error("Error creating tree:", error);
    });
});

// Function to visualize the tree (show the result)
function visualizeTree(data) {
    const resultDiv = document.getElementById("tree-visualization");

    // Example: if a tree image is returned from the backend
    if (data.tree_image) {
        resultDiv.innerHTML = `<img src="/static/${data.tree_image}" alt="BST Visualization">`;
    } else {
        resultDiv.innerHTML = "<p>Tree created successfully!</p>";
    }
}

// Search functionality
document.getElementById("search-btn").addEventListener("click", function() {
    const searchValue = document.getElementById("search-value").value;
    fetch(`/search_bst?value=${searchValue}`)
        .then(response => response.json())
        .then(data => {
            if (data.found) {
                alert(`Value ${searchValue} found in the tree.`);
            } else {
                alert(`Value ${searchValue} not found.`);
            }
        });
});

// Delete functionality
document.getElementById("delete-btn").addEventListener("click", function() {
    const deleteValue = document.getElementById("delete-value").value;
    fetch(`/delete_bst?value=${deleteValue}`, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
        alert(`Value ${deleteValue} deleted.`);
    });
});
