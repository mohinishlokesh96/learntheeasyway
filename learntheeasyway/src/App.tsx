import React from 'react';
import Navigation from './components/Navigation/Navigation';
import './App.css';
import HomePage from './components/HomePage/HomePage';
import MainPage from './components/MainPage/MainPage';
const App=()=> {
  return (
    <div className="App">
      <Navigation/>
      <HomePage/>
      <MainPage/>
    </div>
  );
}

export default App;
