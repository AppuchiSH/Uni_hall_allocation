document.addEventListener("DOMContentLoaded", function () {
    let calendarEl = document.getElementById("calendar");
    let eventListContainer = document.getElementById("event-list");
    let eventDetails = document.getElementById("event-details");

    let calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: "dayGridMonth", // Ensure month grid view on load
        headerToolbar: {
            left: "prev,next today",
            center: "title",
            right: "dayGridMonth,timeGridWeek,timeGridDay,listWeek"
        },
        height: "auto",
        contentHeight: 600,
        aspectRatio: 1.35,
        events: [], // No preloaded events

        dateClick: function (info) {
            eventDetails.innerHTML = `<h4>Events on ${info.dateStr}</h4>`;

            let events = calendar.getEvents().filter(event => event.startStr.startsWith(info.dateStr));

            if (events.length > 0) {
                eventDetails.innerHTML += events.map(event => `
                    <li><strong>${event.title}</strong> - ${event.start.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</li>
                `).join("");
            } else {
                eventDetails.innerHTML += "<li>No events found</li>";
            }

            eventListContainer.style.display = "block"; // Show event panel
        }
    });

    calendar.render(); // Ensure proper rendering

    // Force rerender after showing calendar to fix layout issue
    function showCalendar() {
        let calendarContainer = document.getElementById("calendar-container");
        calendarContainer.style.display = "flex";
        setTimeout(() => {
            calendar.render(); // Rerender after a short delay
        }, 100);
    }

    function closeCalendar() {
        document.getElementById("calendar-container").style.display = "none";
        document.getElementById("event-list").style.display = "none";
    }

    // Assign functions to window so they can be called from HTML
    window.showCalendar = showCalendar;
    window.closeCalendar = closeCalendar;
});
