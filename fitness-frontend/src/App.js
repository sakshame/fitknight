import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import ProfilePage from './pages/Profile';
import LocationList from './components/LocationList';
import FitnessGroupList from './components/FitnessGroupList';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/locations" element={<LocationList />} />
        <Route path="/fitness-groups" element={<FitnessGroupList />} />
        {/* Add more routes as needed */}
      </Routes>
    </Router>
  );
};

export default App;
