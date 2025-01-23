import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/">Dashboard</Link></li>
        <li><Link to="/profile">Profile</Link></li>
        <li><Link to="/locations">Locations</Link></li>
        <li><Link to="/fitness-groups">Fitness Groups</Link></li>
        <li><Link to="/signup">Sign Up</Link></li>  {/* Link to Signup */}
        <li><Link to="/login">Login</Link></li>    {/* Link to Login */}
      </ul>
    </nav>
  );
};

export default Navbar;
