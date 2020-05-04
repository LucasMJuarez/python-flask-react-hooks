import React from 'react';
import { Link } from 'react-router-dom'


export const Navbar = () => {
    return (
        <div>
            <nav className="d-flex justify-content-start navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="d-flex justify-content-center" id="navbarColor02">
                    <h2 className="d-flex nav-title " >CRUD REACT-PYTHON</h2>

                    <ul className="d-flex navbar-nav ml-4">

                        <li className="nav-item active ">
                            <Link className="nav-link" to="/">Users</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/about">About</Link>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
    );
}

