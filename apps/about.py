from dash import html


layout = html.Div([

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Syed Zeshan Bukhari', style={"color": "#0084d6",
                                                 'margin-left': '15px',
                                                 'margin-top': '15px'}),
                    html.P(
                        'Data Scientist with a comprehensive skill set that seamlessly '
                        'combines the roles of Data Engineer and Data Analyst. Seven years '
                        'of work experience with RDX, Lyftron Data, Civil Aviation '
                        'Authority, and National Highway Authority. Knowledge of data '
                        'warehouses and business intelligence tools. Always eager to find '
                        'solutions by thinking out of the box. Has designed and developed '
                        'complex data pipelines, ETL workflows, and dashboards that enable '
                        'organizations to effectively manage and leverage their data.',
                        style={"color": "#ffffff",
                                  "font-size": "15px",
                                  'margin-left': '15px',
                                  'margin-right': '15px',
                                  'margin-top': '15px',
                                  'margin-bottom': '15px',
                                  'line-height': '1.2',
                                  'text-align': 'justify'
                                  }
                           ),
                    html.Div([
                        html.A(href='https://github.com/syedzeshan886-ai', target='_blank',
                               children=[html.Img(src='/assets/github.png', height="30px")]),
                        html.A(href='https://community.plotly.com', target='_blank',
                               children=[html.Img(src='/assets/plotly.ico', height="30px")]),
                        html.A(href='https://www.linkedin.com/in/bukhari886', target='_blank',
                               children=[html.Img(src='/assets/linkedin.png', height="30px")]),
                    ], className='about_social_links')
                ], className='first_text_column'),
                html.Div([
                    html.Img(src='/assets/programmer.gif', className='gif_image')
                ], className='gif_column')
            ], className='gif_row')
        ], className='about_bg eight columns')
    ], className='about_row row')

])
