# MeterGroup

MeterGroup displays scalar measurements within a known range.

## Import [#](https://primevue.org/metergroup/#import)

```

import MeterGroup from 'primevue/metergroup';


```

## Basic [#](https://primevue.org/metergroup/#basic)

MeterGroup requires a *value* as the data to display where each item in the collection should be a type of *MeterItem*.

1. Space used (15%)

```

<MeterGroup :value="value" />


```

## Multiple [#](https://primevue.org/metergroup/#multiple)

Adding more items to the array displays the meters in a group.

1. Apps (16%)
2. Messages (8%)
3. Media (24%)
4. System (10%)

```

<MeterGroup :value="value" />


```

## Icon [#](https://primevue.org/metergroup/#icon)

Icons can be displayed next to the labels instead of the default marker.

1. Apps (16%)
2. Messages (8%)
3. Media (24%)
4. System (10%)

```

<MeterGroup :value="value" />


```

## Label [#](https://primevue.org/metergroup/#label)

The position of the labels relative to the meters is defined using the *labelPosition* property. The default orientation of the labels is horizontal, and the vertical alternative is available through the *labelOrientation* option.

1. Apps (16%)
2. Messages (8%)
3. Media (24%)
4. System (10%)

```

<MeterGroup :value="value" labelPosition="start" labelOrientation="vertical" />


```

## Vertical [#](https://primevue.org/metergroup/#vertical)

Layout of the MeterGroup is configured with the *orientation* property that accepts either *horizontal* or *vertical* as available options.

1. Apps (24%)
2. Messages (16%)
3. Media (24%)
4. System (12%)

```

<MeterGroup :value="value" orientation="vertical" labelOrientation="vertical" />


```

## Min-Max [#](https://primevue.org/metergroup/#minmax)

Boundaries are configured with the *min* and *max* values whose defaults are 0 and 100 respectively.

1. Apps (8%)
2. Messages (4%)
3. Media (12%)
4. System (5%)

```

<MeterGroup :value="value" :max="200"  />


```

## Template [#](https://primevue.org/metergroup/#template)

MeterGroup provides templating support for labels, meter items, and content around the meters.

Apps25%

Messages15%

Media20%

System10%

Storage70%1TB

Manage StorageUpdate Plan

```

<MeterGroup :value="value" labelPosition="start">
    <template #label="{ value }">
        <div class="flex flex-wrap gap-4">
            <template v-for="val of value" :key="val.label">
                <Card class="flex-1 border border-surface shadow-none">
                    <template #content>
                        <div class="flex justify-between gap-8">
                            <div class="flex flex-col gap-1">
                                <span class="text-surface-500 dark:text-surface-400 text-sm">{{ val.label }}</span>
                                <span class="font-bold text-lg">{{ val.value }}%</span>
                            </div>
                            <span class="w-8 h-8 rounded-full inline-flex justify-center items-center text-center" :style="{ backgroundColor: `${val.color1}`, color: '#ffffff' }">
                                <i :class="val.icon" />
                            </span>
                        </div>
                    </template>
                </Card>
            </template>
        </div>
    </template>
    <template #meter="slotProps">
        <span :class="slotProps.class" :style="{ background: `linear-gradient(to right, ${slotProps.value.color1}, ${slotProps.value.color2})`, width: slotProps.size }" />
    </template>
    <template #start="{ totalPercent }">
        <div class="flex justify-between mt-4 mb-2 relative">
            <span>Storage</span>
            <span :style="{ width: totalPercent + '%' }" class="absolute text-right">{{ totalPercent }}%</span>
            <span class="font-medium">1TB</span>
        </div>
    </template>
    <template #end>
        <div class="flex justify-between mt-4">
            <Button label="Manage Storage" variant="outlined" size="small" />
            <Button label="Update Plan" size="small" />
        </div>
    </template>
</MeterGroup>


```

## Accessibility [#](https://primevue.org/metergroup/#accessibility)

### Screen Reader

MeterGroup component uses *meter* role in addition to the *aria-valuemin*, *aria-valuemax* and *aria-valuenow* attributes. Value to describe the component can be defined using *aria-labelledby* prop.

### Keyboard Support

Component does not include any interactive elements.