import React, { useState } from 'react';
import axios from 'axios';

function EventForm({ onEventAdded }) {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [startTime, setStartTime] = useState('');
    const [endTime, setEndTime] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const event = { title, description, start_time: startTime, end_time: endTime };
        await axios.post('/api/events', event);
        onEventAdded();
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} />
            <input type="text" placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
            <input type="datetime-local" value={startTime} onChange={(e) => setStartTime(e.target.value)} />
            <input type="datetime-local" value={endTime} onChange={(e) => setEndTime(e.target.value)} />
            <button type="submit">Add Event</button>
        </form>
    );
}

export default EventForm;
