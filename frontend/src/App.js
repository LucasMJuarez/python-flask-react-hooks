import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { About } from './components/About'
import { Users } from './components/Users'
import { Navbar } from './components/Navbar'
import Footer from './components/Footer';


function App() {
  return (
    <Router>
      <Navbar />
      <div className="container p-2">
        <Switch>
          <Route path="/about" component={About} />
          <Route path="/" component={Users} />
        </Switch>
      </div>
      <Footer />
    </Router>
  );
}

export default App;
