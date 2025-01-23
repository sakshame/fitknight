import React, { useEffect, useState } from 'react';
import { getUsers } from '../services/api';

const UserList = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    getUsers()
      .then(response => {
        setUsers(response.data);
      })
      .catch(error => {
        console.error('Error fetching users:', error);
      });
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Users</h2>
      <ul className="space-y-4">
        {users.map(user => (
          <li key={user.id} className="bg-gray-100 p-4 rounded shadow">
            <p className="font-semibold">{user.username}</p>
            <p>{user.email}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserList;
