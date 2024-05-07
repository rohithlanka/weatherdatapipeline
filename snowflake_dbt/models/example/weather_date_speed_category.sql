SELECT 
    place,
    {{ generate_date_format() }},
    {{ generate_time_format() }},
    weather,
    {{ generate_wind_speed_category() }},
    temp 
FROM {{ ref('basic_weather')}}