let selectedFeature; // Store the feature name being edited
let statusElement; // Store the element to update after change

// Function to open the modal when the status is clicked
function openModal(featureName, element) {
    selectedFeature = featureName; // Store the clicked feature name
    statusElement = element; // Store the element to update

    document.getElementById('modalFeatureName').innerText = featureName;
    document.getElementById('statusModal').style.display = "block"; // Show modal
}

// Function to close the modal
function closeModal() {
    document.getElementById('statusModal').style.display = "none"; // Hide modal
}

// Function to update the status after selecting an option
function updateStatus() {
    const selectedOption = document.querySelector('input[name="statusOption"]:checked')?.value;
    
    // Check if an option is selected and update the status
    if (selectedOption) {
        statusElement.innerText = selectedOption; // Update the status on the page
    }

    const selectedTopic = document.getElementById('topicsSelect')?.value;
    
    // Handle 'Only in these topics' dropdown selection (if needed)
    if (selectedTopic) {
        console.log('Selected topic:', selectedTopic);
    }

    closeModal(); // Close the modal after update

    document.getElementById('topicsSelect').addEventListener('change', function() {
        const selectedTopic = this.value;
        if (selectedTopic === "") {
            console.log("Please select a topic");  // Log if no topic is selected
        } else {
            console.log("Selected Topic:", selectedTopic);  // Log the selected topic
        }
    });
    
}
