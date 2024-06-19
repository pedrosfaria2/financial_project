import React from 'react';
import Events from './components/Events';
import Users from './components/Users';

function App() {
    return (
        <div className="App">
            <h1>Financial Event Notification</h1>
            <Events />
            <Users />
        </div>
    );
}

export default App;
