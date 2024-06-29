import React, { useState, useEffect } from 'react';
import { getUsersList } from '../services/UserService';
import UserCard from './UserCard';
import './style/body.css'


const Body = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const usersData = await getUsersList();
        setUsers(usersData);
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    };

    fetchUsers();
  }, []);

  return (
    <div className='body_content'>
      {users.map(user => (
        <UserCard 
          
          key={user.id} 
          firstname={user.firstName} 
          lastname={user.lastName} 
          username={user.userName} 
        />
      ))}
    </div>
  );
};

export default Body;
