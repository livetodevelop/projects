// Homework Tracker Logic

let assignments = JSON.parse(localStorage.getItem('assignments')) || [];

function addAssignment() {
    const title = document.getElementById('title').value;
    const subject = document.getElementById('subject').value;
    const dueDate = document.getElementById('dueDate').value;
    const notes = document.getElementById('notes').value;
    
    if (!title || !dueDate) {
        alert('Please fill in title and due date');
        return;
    }
    
    assignments.push({
        id: Date.now(),
        title,
        subject,
        dueDate,
        notes,
        completed: false
    });
    
    saveAndRender();
    clearForm();
}

function deleteAssignment(id) {
    assignments = assignments.filter(a => a.id !== id);
    saveAndRender();
}

function toggleComplete(id) {
    const assignment = assignments.find(a => a.id === id);
    if (assignment) {
        assignment.completed = !assignment.completed;
        saveAndRender();
    }
}

function saveAndRender() {
    localStorage.setItem('assignments', JSON.stringify(assignments));
    renderAssignments();
}

function renderAssignments() {
    const container = document.getElementById('assignments');
    const dueSoonContainer = document.getElementById('dueSoon');
    
    const today = new Date();
    const threeDaysFromNow = new Date(today);
    threeDaysFromNow.setDate(threeDaysFromNow.getDate() + 3);
    
    let dueSoonHTML = '';
    let allHTML = '';
    
    assignments.forEach(a => {
        const due = new Date(a.dueDate);
        const daysUntilDue = Math.ceil((due - today) / (1000 * 60 * 60 * 24));
        
        let statusClass = '';
        if (daysUntilDue < 0) statusClass = 'overdue';
        else if (daysUntilDue <= 3) statusClass = 'due-soon';
        
        const html = `
            <div class="assignment ${statusClass} ${a.completed ? 'completed' : ''}">
                <strong>${a.title}</strong><br>
                <small>${a.subject} | Due: ${a.dueDate}</small><br>
                ${a.notes ? `<small>${a.notes}</small><br>` : ''}
                <button onclick="toggleComplete(${a.id})">${a.completed ? '↩️ Undo' : '✅ Complete'}</button>
                <button class="delete-btn" onclick="deleteAssignment(${a.id})">Delete</button>
            </div>
        `;
        
        if (daysUntilDue >= 0 && daysUntilDue <= 3 && !a.completed) {
            dueSoonHTML += html;
        }
        allHTML += html;
    });
    
    dueSoonContainer.innerHTML = dueSoonHTML || '<p>No assignments due soon!</p>';
    container.innerHTML = allHTML || '<p>No assignments yet.</p>';
}

function clearForm() {
    document.getElementById('title').value = '';
    document.getElementById('subject').value = '';
    document.getElementById('dueDate').value = '';
    document.getElementById('notes').value = '';
}

function exportData() {
    const dataStr = JSON.stringify(assignments, null, 2);
    const blob = new Blob([dataStr], {type: 'application/json'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'homework-backup.json';
    a.click();
}

function clearAll() {
    if (confirm('Are you sure? This will delete all assignments!')) {
        assignments = [];
        saveAndRender();
    }
}

// Initial render
renderAssignments();
