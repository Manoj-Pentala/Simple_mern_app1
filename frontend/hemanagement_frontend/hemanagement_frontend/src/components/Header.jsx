import { Link, useLocation, useNavigate } from 'react-router-dom';
import './Header.css';

function Header() {
  const location = useLocation();
  const navigate = useNavigate();

  let currentuser = null;
  try {
    currentuser = JSON.parse(localStorage.getItem('currentUser') || 'null');
  } catch {
    localStorage.removeItem('currentUser');
  }

  const handleLogout = () => {
    localStorage.removeItem('currentUser');
    navigate('/login');
  };

  return (
    <div className="header">
      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
      <Link to="/contact">Contact</Link>

      {!currentuser && (
        <div>
          <Link to="/login">Login</Link>
          <Link to="/register">Register</Link>
        </div>
      )}

      {currentuser?.role === 'HR' && (
        <div>
          <Link to="#">Assign task</Link>
          <Link to="#">View employees</Link>
          <button onClick={handleLogout}>Logout</button>
        </div>
      )}

      {currentuser?.role === 'admin' && (
        <div>
          <Link to="#">View employees</Link>
          <Link to="#">View tasks</Link>
          <button onClick={handleLogout}>Logout</button>
        </div>
      )}
    </div>
  );
}

export default Header;