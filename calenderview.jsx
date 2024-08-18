import React, { useState, useEffect } from 'react';
import Calendar from 'react-calendar';
import axios from 'axios';

function CalendarView() {
    const [date, setDate] = useState(new Date());
    const [events, setEvents] = useState([]);

    useEffect(() => {
        axios.get('/api/events').then(response => {
            setEvents(response.data);
        });
    }, []);

    return (
        <div>
            <Calendar
                onChange={setDate}
                value={date}
                tileContent={({ date }) => {
                    const event = events.find(e => new Date(e.start_time).toDateString() === date.toDateString());
                    return event ? <p>{event.title}</p> : null;
                }}
            />
        </div>
    );
}

export default CalendarView;
