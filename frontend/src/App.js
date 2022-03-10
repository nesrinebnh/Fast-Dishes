import React , { useEffect, useState } from 'react';
import "./App.css";
import Card from "./components/Card";
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';

function App() {
  const recipeAuthor = "Efecan";
 

  const like= 193;
  const isLiked = true;
  const [search, setSearch] = useState(false)
  const [options, setOptions] = useState(['search for title'])
  const [Recipe, setRecipe] = useState([]);
  const [value, setValue] = useState(options[0]);
  const [inputValue, setInputValue] = useState('');
  //Get the authentificated user
  useEffect(()=>{
    (
      async()=>{
        var url = ''
        if(search===false)
        {
          url = 'http://localhost:8000/api/recipes/fetch'
        }else{
          url = 'http://localhost:8000/api/recipes/recipes/'+value
        }
        console.log('url: ', url);
        const response = await fetch(url, {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
            credentials: 'include',//To get the cookie
        })

        const content = await response.json()
        console.log(content)
        if(search === false){
          const options1 = []
          content.forEach(element => {
            options1.push(element['title'])
          
          });
          const arr = []
          Object.keys(content).forEach(key => arr.push({name: key, value: content[key]}))
          console.log("arr: ", arr)
          console.log("options: ", options1)
          setRecipe(arr)
          setOptions(options1)
        }else{
          console.log('content tyoe: ', typeof content)
          const arr = []
          arr.push({value: content})
          //Object.keys(content).forEach(key => arr.push({name: key, value: content[key]}))
          console.log('arr: ', arr)
          setRecipe(arr)
          console.log("options: ", options)
          
        }
        
      }
    )();
  }, [search])

  return (
    <div className="App">
      
      <header className="App-header">
        <div>
          <br />
          <Autocomplete
            value={value}
            onChange={(event, newValue) => {
              setSearch(true);
              setValue(newValue);
              
              
            }}
            inputValue={inputValue}
            onInputChange={(event, newInputValue) => {
              setSearch(false);
              setInputValue(newInputValue);
            }}
            id="controllable-states-demo"
            options={options}
            sx={{ width: 300 }}
            renderInput={(params) => <TextField {...params} label="Search" />}
          />
        </div>
        {Recipe.map(function(d, idx){
          
          return (
            <Card
              key = {idx}
              author={recipeAuthor}
              title={d.value.title}
              date={d.value.duration}
              description={d.value.description}
              liked={isLiked}
              likeCount={like}
              image={d.value.url}
              level={d.value.level}
            />
          )
        })}
        
      </header>
    </div>
  );
}

export default App;
