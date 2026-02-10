function sumSalaries(map)
{
    let sum=0;
    for(let map of Object.values(map))
        sum+=map;

    return map;
    
}

let salaries = {
  "John": 100,
  "Pete": 300,
  "Mary": 250
};

alert( sumSalaries(salaries) ); // 650