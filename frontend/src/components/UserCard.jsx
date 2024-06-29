import React from 'react'
import './style/card.css'

const UserCard = (props) => {
  return (
    <div className='user_card'>
      <p>fName: {props.firstname}</p>
      <p>lName:{props.lastname}</p>
      <p>uName:{props.username}</p>
    </div>
  )
}

export default UserCard
