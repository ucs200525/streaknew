// script.js
document.getElementById('topicSelect').addEventListener('change', function() {
    var choice = this.value;
    var innerChoices = document.getElementById('innerChoices');
    innerChoices.innerHTML = '';

    var options = {
        1: ['HTML', 'CSS', 'JS', 'JAVA(JDBC)'],
        2: ['FRONTEND', 'BACKEND', 'COURSE'],
        3: ['10 grades', 'gate', 'internship', 'placements'],
        4: ['Meditation', 'Video Editing', 'Duolingo'],
        5: ['Cyber Security']
    };

    if (choice == 1) {
        options[1].forEach(function(innerChoice, index) {
            var input = document.createElement('input');
            input.type = 'checkbox';
            input.name = 'inner_choice';
            input.value = innerChoice;
            innerChoices.appendChild(input);

            var space = document.createElement('span');
            space.innerHTML = '&nbsp;&nbsp;'; // Add space between checkbox and label
            innerChoices.appendChild(space);

            var label = document.createElement('label');
            label.textContent = innerChoice;
            innerChoices.appendChild(label);
        });
    } else {
        options[choice].forEach(function(innerChoice, index) {
            var input = document.createElement('input');
            input.type = 'checkbox';
            input.name = 'inner_choice';
            input.value = innerChoice;
            innerChoices.appendChild(input);

            var space = document.createElement('span');
            space.innerHTML = '&nbsp;&nbsp;'; // Add space between checkbox and label
            innerChoices.appendChild(space);

            var label = document.createElement('label');
            label.textContent = innerChoice;
            innerChoices.appendChild(label);
        });
    }
});

document.querySelectorAll('input[name="descriptionChoice"]').forEach(function(radio) {
    radio.addEventListener('change', function() {
        var descriptionField = document.getElementById('descriptionField');
        if (this.value === 'yes') {
            descriptionField.style.display = 'block';
        } else {
            descriptionField.style.display = 'none';
        }
    });
});
