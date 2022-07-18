import { Route, Routes, Router, Redirect } from 'react-router-dom'

const PrivateRoute = ({ children, ...rest }) => {
    console.log('private route works')
    /* const authenticated = false */
    return (
        <Router>
            <Routes>
                <Route {...rest}>{children}</Route>
            </Routes>
        </Router>

    )
}

export default PrivateRoute;