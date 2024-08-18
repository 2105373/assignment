import React, { useEffect, useState } from 'react';
import axios from 'axios';

function EventList() {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        axios.get('/api/events').then(response => {
            setEvents(response.data);
        });
    }, []);

    return (
        <ul>
            {events.map(event => (
                <li key={event.id}>
                    {event.title} - {new Date(event.start_time).toLocaleString()} to {new Date(event.end_time).toLocaleString()}
                </li>
            ))}
        </ul>
    );
}

export default EventList;
