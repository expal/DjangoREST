import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import axios from 'axios'
import Menu from "./components/Menu";
import Footer from "./components/Footer";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors')
            .then(response => {
                const authors = response.data
                this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error))
    }


    render() {
        return (
            <div>
                <AuthorList authors={this.state.authors}/>
                <Menu></Menu>
                <Footer></Footer>
            </div>
        )
    }
}



export default App;
