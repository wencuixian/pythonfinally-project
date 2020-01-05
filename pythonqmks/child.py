from flask import Flask, render_template, request
from pyecharts.charts import Bar, Grid, Line, Scatter, Geo, Map, Timeline, Page, Funnel, Pie
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType

df1 = pd.read_csv("flask.csv", encoding='gbk')

app = Flask(__name__)

# 准备工作
regions_available = list(df1.CountryName.dropna().unique())


def getCsvData(filePath):
    """
    获取csv表格数据
    """
    df = pd.read_csv(filePath, encoding='GBK')
    df.fillna(0, inplace=True)
    return df


def map_world_gdp(df) -> Map:
    """
    获取世界各国GDP Map数据
    """
    c = (
        Map()
            .add("世界各国GDP", [list(n) for n in zip(list(df.Country), list(df['2019']))], "world")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="世界各国GDP"),
            visualmap_opts=opts.VisualMapOpts(max_=10000000000000),
        )
    )
    return c


def pie_base(df) -> Pie:
    """
    获取各国GDP饼状图
    """
    c = (
        Pie()
            .add("", [list(b) for b in zip(list(df.sn), list(df.money))])
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c


def line_markpoint(df) -> Line:
    """
    获取折线图
    """
    c = (
        Line()
            .add_xaxis(list(df.sn))
            .add_yaxis(
            "GDP",
            list(df.money),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
        )
            .add_yaxis(
            "dependency",
            list(df.dependency),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint"))
    )
    return c


def bar_datazoom_select(df) -> Bar:
    """
    获取slider-水平柱状图
    """
    c = (
        Bar()
            .add_xaxis(list(df.sn))
            .add_yaxis("GDP", list(df.money))
            .add_yaxis("dependency", list(df.dependency), is_selected=False)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


@app.route('/', methods=['GET'])
def hu_run_2019():
    data_str = df1.to_html()
    return render_template('results2.html',
                           the_res=data_str,
                           the_select_region=regions_available)


@app.route('/hurun', methods=['POST'])
def hu_run_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region)  # 检查用户输入
    dfs = df1.query("CountryName=='{}'".format(the_region))

    gdp_df = getCsvData('GDP.csv')  # 读取GDP.csv 数据内容
    select_df = getCsvData('select_nation.csv')  # 读取select_nation.csv 数据内容
    fig1 = map_world_gdp(gdp_df)
    fig2 = pie_base(select_df)
    fig3 = bar_datazoom_select(select_df)
    fig4 = line_markpoint(select_df)

    page = Page(layout=Page.SimplePageLayout)
    page.add(fig1, fig2, fig3, fig4)
    page.render("child2.html")

    with open("templates/child2.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    data_str = dfs.to_html()
    return render_template('results2.html',
                           the_plot_all=plot_all,
                           the_res=data_str,
                           the_select_region=regions_available,
                           )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
