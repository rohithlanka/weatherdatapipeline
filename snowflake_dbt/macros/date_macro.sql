{% macro generate_date_format() %}
to_date(date)
AS date_format
  -- Using dbt's ref function to reference the films table
{% endmacro %}