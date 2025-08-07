# Timeline

Timeline visualizes a series of chained events.

## Import [#](https://primevue.org/timeline/#import)

```

import Timeline from 'primevue/timeline';


```

## Basic [#](https://primevue.org/timeline/#basic)

Timeline requires a *value* for the collection of events and *content* slot that receives an object as a parameter to return content.

Ordered

Processing

Shipped

Delivered

```

<Timeline :value="events">
    <template #content="slotProps">
        {{ slotProps.item.status }}
    </template>
</Timeline>


```

## Alignment [#](https://primevue.org/timeline/#alignment)

Content location relative the line is defined with the *align* property.

Ordered

Processing

Shipped

Delivered

Ordered

Processing

Shipped

Delivered

Ordered

Processing

Shipped

Delivered

```

<Timeline :value="events" class="w-full md:w-80">
    <template #content="slotProps">
        {{ slotProps.item.status }}
    </template>
</Timeline>

<Timeline :value="events" align="right" class="w-full md:w-80">
    <template #content="slotProps">
        {{ slotProps.item.status }}
    </template>
</Timeline>

<Timeline :value="events" align="alternate" class="w-full md:w-80">
    <template #content="slotProps">
        {{ slotProps.item.status }}
    </template>
</Timeline>


```

## Opposite [#](https://primevue.org/timeline/#opposite)

Additional content at the other side of the line can be provided with the *opposite* property.

15/10/2020 10:30

Ordered

15/10/2020 14:00

Processing

15/10/2020 16:15

Shipped

16/10/2020 10:00

Delivered

```

<Timeline :value="events">
    <template #opposite="slotProps">
        <small class="text-surface-500 dark:text-surface-400">{{slotProps.item.date}}</small>
    </template>
    <template #content="slotProps">
        {{slotProps.item.status}}
    </template>
</Timeline>


```

## Template [#](https://primevue.org/timeline/#template)

Sample implementation with custom content and styled markers.

Ordered

15/10/2020 10:30

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!

Read more

Processing

15/10/2020 14:00

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!

Read more

Shipped

15/10/2020 16:15

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!

Read more

Delivered

16/10/2020 10:00

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!

Read more

```

<Timeline :value="events" align="alternate" class="customized-timeline">
    <template #marker="slotProps">
        <span class="flex w-8 h-8 items-center justify-center text-white rounded-full z-10 shadow-sm" :style="{ backgroundColor: slotProps.item.color }">
            <i :class="slotProps.item.icon"></i>
        </span>
    </template>
    <template #content="slotProps">
        <Card class="mt-4">
            <template #title>
                {{ slotProps.item.status }}
            </template>
            <template #subtitle>
                {{ slotProps.item.date }}
            </template>
            <template #content>
                <img v-if="slotProps.item.image" :src="`/images/product/${slotProps.item.image}`" :alt="slotProps.item.name" width="200" class="shadow-sm" />
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate
                    neque quas!
                </p>
                <Button label="Read more" variant="text"></Button>
            </template>
        </Card>
    </template>
</Timeline>


```

## Horizontal [#](https://primevue.org/timeline/#horizontal)

TimeLine orientation is controlled with the *layout* property, default is *vertical* having *horizontal* as the alternative.

2020

2021

2022

2023

2020

2021

2022

2023

2020

2021

2022

2023

```

<Timeline :value="events" layout="horizontal" align="top">
    <template #content="slotProps">
        {{ slotProps.item }}
    </template>
</Timeline>

<Timeline :value="events" layout="horizontal" align="bottom">
    <template #content="slotProps">
        {{ slotProps.item }}
    </template>
</Timeline>

<Timeline :value="events" layout="horizontal" align="alternate">
    <template #opposite> &nbsp; </template>
    <template #content="slotProps">
        {{ slotProps.item }}
    </template>
</Timeline>


```

## Accessibility [#](https://primevue.org/timeline/#accessibility)

### Screen Reader

Timeline uses a semantic ordered list element to list the events. No specific role is enforced, still you may use any aria role and attributes as any valid attribute is passed to the list element.

### Keyboard Support

Component does not include any interactive elements.