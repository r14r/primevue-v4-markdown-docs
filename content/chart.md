# Chart

Chart components are based on Chart.js, an open source HTML5 based charting library.

## Import [#](https://primevue.org/chart/#import)

```

import Chart from 'primevue/chart';


```

## Chart.js [#](https://primevue.org/chart/#chartjs)

Chart component uses [Chart.JS](https://chartjs.org/) underneath so it needs to be installed as a dependency.

```

npm install chart.js


```

## Basic [#](https://primevue.org/chart/#basic)

A chart is configured with 3 properties; *type*, *data* and *options*. Chart type is defined using the *type* property that accepts *pie*, *doughtnut*, *line*, *bar*, *radar* and *polarArea* as a value. The *data* defines datasets represented with the chart and the *options* provide numerous customization options to customize the presentation.

```

<Chart type="bar" :data="chartData" :options="chartOptions" />


```

## Pie [#](https://primevue.org/chart/#pie)

A pie chart is a circular statistical graphic which is divided into slices to illustrate numerical proportion.

```

<Chart type="pie" :data="chartData" :options="chartOptions" class="w-full md:w-[30rem]" />


```

## Doughnut [#](https://primevue.org/chart/#doughnut)

A doughnut chart is a variant of the pie chart, with a blank center allowing for additional information about the data as a whole to be included.

```

<Chart type="doughnut" :data="chartData" :options="chartOptions" class="w-full md:w-[30rem]" />


```

## Vertical Bar [#](https://primevue.org/chart/#vertical)

A bar chart or bar graph is a chart that presents grouped data with rectangular bars with lengths proportional to the values that they represent.

```

<Chart type="bar" :data="chartData" :options="chartOptions" class="h-[30rem]"  />


```

## Horizontal Bar [#](https://primevue.org/chart/#horizontal)

A bar chart is rendered horizontally when *indexAxis* option is set as *y*.

```

<Chart type="bar" :data="chartData" :options="chartOptions" class="h-[30rem]"  />


```

## Stacked Bar [#](https://primevue.org/chart/#stacked)

Bars can be stacked on top of each other when *stacked* option of a scale is enabled.

```

<Chart type="bar" :data="chartData" :options="chartOptions" class="h-[30rem]" />


```

## Line [#](https://primevue.org/chart/#line)

A line chart or line graph is a type of chart which displays information as a series of data points called 'markers' connected by straight line segments.

```

<Chart type="line" :data="chartData" :options="chartOptions" class="h-[30rem]" />


```

## Multi Axis [#](https://primevue.org/chart/#multiaxis)

Multiple axes can be added using the *scales* option.

```

<Chart type="line" :data="chartData" :options="chartOptions" class="h-[30rem]" />


```

## Line Styles [#](https://primevue.org/chart/#linestyles)

Various styles of a line series can be customized to display customizations like an area chart.

```

<Chart type="line" :data="chartData" :options="chartOptions" class="h-[30rem]" />


```

## Polar Area [#](https://primevue.org/chart/#polararea)

Polar area charts are similar to pie charts, but each segment has the same angle - the radius of the segment differs depending on the value.

```

<Chart type="polarArea" :data="chartData" :options="chartOptions" class="w-full md:w-[30rem]" />


```

## Radar [#](https://primevue.org/chart/#radar)

A radar chart is a graphical method of displaying multivariate data in the form of a two-dimensional chart of three or more quantitative variables represented on axes starting from the same point.

```

<Chart type="radar" :data="chartData" :options="chartOptions" class="w-full md:w-[30rem]" />


```

## Combo [#](https://primevue.org/chart/#combo)

Different chart types can be combined in the same graph usign the *type* option of a dataset.

```

<Chart type="bar" :data="chartData" :options="chartOptions" class="h-[30rem]" />


```

## Accessibility [#](https://primevue.org/chart/#accessibility)

### Screen Reader

Chart components internally use *canvas* element, refer to the [Chart.js accessibility](https://www.chartjs.org/docs/latest/general/accessibility.html) guide for more information. The canvas element can be customized with *canvasProps* property to define aria roles and properties, in addition any content inside the component is directly passed as a child of the canvas to be able to provide fallback content like a table.

```

<Chart type="line" :data="data" :canvasProps="{'role': 'img', 'aria-label': 'Data'}" />


```