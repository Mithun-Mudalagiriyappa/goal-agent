import React, { useState } from "react";

function GoalInput({ onSubmit }) {
    const [goal, setGoal] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (goal.trim()) {
            onSubmit(goal);
            setGoal('');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Enter your goal"
                value={goal}
                onChange={(e) => setGoal(e.target.value)}
                style={{ padding: '10px', width: '80%', marginRight: '10px' }}
            />
            <button type="submit">Generate Tasks</button>
        </form>
    );
}

export default GoalInput;