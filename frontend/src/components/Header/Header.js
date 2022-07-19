import React, { useContext } from 'react'
import AuthContext from '../../context/AuthContext'
import { Navbar, Container, Nav } from "react-bootstrap";

const Header = () => {
    let { user, logoutUser } = useContext(AuthContext)
    return (
        <div className="App">
            <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
                <Container>
                    <Navbar.Brand href="#home" >ТЮМГУ</Navbar.Brand>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse id="responsive-navbar-nav">
                        <Nav className="me-auto">
                            <Nav.Link href="#features">Посещения</Nav.Link>
                            <Nav.Link href="#pricing">Расписание</Nav.Link>

                        </Nav>
                        <Nav>
                            {user ? (
                                <Nav.Link href="#deets" onClick={logoutUser}>Выйти</Nav.Link>
                            ) : (
                                <Nav.Link to="/login" >Login</Nav.Link>
                            )}
                            
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </div>
    );
}


export default Header