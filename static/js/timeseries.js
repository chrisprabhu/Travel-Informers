
function DropDown() {
    let url = "/city_attributes"
    let dropDownList = Plotly.d3.select("selCity")
                                

    Plotly.d3.json(url, function(error, cities){
        if (error) throw error;
        console.log("city list", cities.keys)
        dropDownList.selectAll('option')
            .data(cities.keys)
            .enter()
            .append('option')
            .text(function (d) { return d; });
    });

let temp_csv = 'historical-hourly-weather-data/daily_avg_temps.csv'

Plotly.d3.csv(temp_csv, function(error, tempData){

    if (error) console.error;

    console.log(tempData.keys);

    function unpack(rows, key){
        return rows.map(function(row){return row[key];});
    }

    let trace1 = {
        type: "scatter",
        mode: "lines",
        name: "Avg temp",
        x: unpack(tempData, 'datetime'),
        y: unpack(tempData, 'Los Angeles'),
        line: {color: '#7F7F7F'}
    }

    let data = [trace1]

    let layout = {
        title: "Average Daily Temperature"
    }

    Plotly.newPlot('timeseries', data, layout)

})