from flask import Flask, abort, jsonify, request, render_template


import rpy2.robjects as robjects
app = Flask(__name__)


 

@app.route('/')
def home():
    return render_template('index.html')
 

@app.route('/api',methods=['POST'])
def get_delay():

    result=request.form.to_dict()
    rstrings = """
    abc <- function(dt)
    {
      library(prophet)
      library(lubridate)
      library(ggplot2)
      library(readr)
      f <- ymd(dt)
      data <- read_csv("/Users/kashikawanchoo/Desktop/Bitcoin/App/criptoes10.csv", 
                   col_types = cols(close = col_number()))
      data$Date <- mdy(data$Date)
      ds <- data$Date
      y <- log(data$close)
      df <- data.frame(ds, y)
      z <- f-data$Date[1]
      m <- prophet(df)
      future <- make_future_dataframe(m, periods = z)
      forecast <- predict(m, future)
      print(exp(forecast[nrow(forecast),'yhat']))
    }
    """
    r = robjects.r(rstrings)
    x = r(str(result['Year']))
    
    return render_template('result.html', data=x[0])

 

if __name__ == '__main__':
    app.run(port=8080, debug=True)








