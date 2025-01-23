import React from 'react';

const FitnessGroupList = ({ users }) => {
  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Fitness Groups</h2>
      <ul>
        {users.map((user) => (
          <li key={user.id} className="mb-2">
            {user.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FitnessGroupList;
