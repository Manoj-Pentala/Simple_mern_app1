import { Link } from "react-router-dom";
import './Header.css'
function Header() {
    return (
        <div className="header">
            <Link to="/">Home</Link>
            <Link to="/about">About</Link>
            <Link to="/contact">Contact</Link>
            <Link to="/services">Services</Link>
            <Link to="/adminlogin">Adminlogin</Link>

        </div>
    )
}
export default Header;