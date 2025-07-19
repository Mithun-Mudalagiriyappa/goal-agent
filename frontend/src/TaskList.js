import React from 'react';

function TaskList({ tasks }) {
  return (
    <ul style={{ listStyleType: 'none', paddingLeft: 0, marginTop: '20px' }}>
      {tasks.map((task, index) => (
        <li key={index} style={{ padding: '5px 0' }}>
          {task}
        </li>
      ))}
    </ul>
  );
}

export default TaskList;