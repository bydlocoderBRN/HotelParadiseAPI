import { Component } from 'react';
import {Cal} from '../components/Calendar/Cal';
import Footer from '../components/Footer/Footer';
import { MainPage } from '../components/MainPage/MainPage';
import { RoomDescription } from '../components/RoomsDescription/RoomDescription';
import './App.scss';

class App extends Component{
    
    

    render(){
        return (
        <div className="app">
          <MainPage/>
          <RoomDescription />
          <Cal />
          <Footer />
        </div>
    );
}
}

export default App;