# OrganizationChart

OrganizationChart visualizes hierarchical organization data.

## Import [#](https://primevue.org/organizationchart/#import)

```

import OrganizationChart from 'primevue/organizationchart';


```

## Basic [#](https://primevue.org/organizationchart/#basic)

OrganizationChart requires a collection of *TreeNode* instances as a *value*.

|  |  |  |  |
| --- | --- | --- | --- |
| Argentina | | | |
|  | | | |
|  |  |  |  |
| |  |  |  |  | | --- | --- | --- | --- | | Argentina | | | | |  | | | | |  |  |  |  | | |  | | --- | | Argentina | |  | | | | | |  | | --- | | Croatia | |  | | | | | | | |  |  |  |  | | --- | --- | --- | --- | | France | | | | |  | | | | |  |  |  |  | | |  | | --- | | France | |  | | | | | |  | | --- | | Morocco | |  | | | | | | |

```

<OrganizationChart :value="data">
    <template #default="slotProps">
        <span>{{ slotProps.node.label }}</span>
    </template>
</OrganizationChart>


```

## Template [#](https://primevue.org/organizationchart/#template)

The *type* property of an OrganizationChartNode is used to map a template to a node. If it is undefined, the default template is used.

|  |  |  |  |
| --- | --- | --- | --- |
| Argentina | | | |
|  | | | |
|  |  |  |  |
| |  |  |  |  | | --- | --- | --- | --- | | Argentina | | | | |  | | | | |  |  |  |  | | |  | | --- | | Argentina | |  | | | | | |  | | --- | | Croatia | |  | | | | | | | |  |  |  |  | | --- | --- | --- | --- | | France | | | | |  | | | | |  |  |  |  | | |  | | --- | | France | |  | | | | | |  | | --- | | Morocco | |  | | | | | | |

```

<OrganizationChart :value="data" collapsible>
    <template #country="slotProps">
        <div class="flex flex-col items-center">
            <img :alt="slotProps.node.label" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`w-2rem flag flag-${slotProps.node.data}`" />
            <div class="mt-4 font-medium text-lg">{{ slotProps.node.label }}</div>
        </div>
    </template>
    <template #default="slotProps">
        <span>{{slotProps.node.data.label}}</span>
    </template>
</OrganizationChart>


```

## Selection [#](https://primevue.org/organizationchart/#selection)

Selection is enabled by defining the *selectionMode* to either "single" or "multiple" and specifying the *selectionKeys* with the v-model directive. Note that selection on a particular node can be disabled if the *selectable* is false on the node instance.

|  |  |  |  |
| --- | --- | --- | --- |
| Amy ElsnerCEO | | | |
|  | | | |
|  |  |  |  |
| |  |  |  |  | | --- | --- | --- | --- | | Anna FaliCMO | | | | |  | | | | |  |  |  |  | | |  | | --- | | Sales | |  | | | | | |  | | --- | | Marketing | |  | | | | | | | |  |  |  |  | | --- | --- | --- | --- | | Stephen ShawCTO | | | | |  | | | | |  |  |  |  | | |  | | --- | | Development | |  | | | | | |  | | --- | | UI/UX Design | |  | | | | | | |

```

<OrganizationChart v-model:selectionKeys="selection" :value="data" collapsible selectionMode="multiple">
    <template #person="slotProps">
        <div class="flex flex-col">
            <div class="flex flex-col items-center">
                <img :alt="slotProps.node.data.name" :src="slotProps.node.data.image" class="mb-4 w-12 h-12" />
                <span class="font-bold mb-2">{{ slotProps.node.data.name }}</span>
                <span>{{ slotProps.node.data.title }}</span>
            </div>
        </div>
    </template>
    <template #default="slotProps">
        <span>{{ slotProps.node.label }}</span>
    </template>
</OrganizationChart>


```

## Colored [#](https://primevue.org/organizationchart/#colored)

Styling a specific node is configured with *styleClass* and *style* options of a TreeNode.

|  |  |  |  |
| --- | --- | --- | --- |
| Amy ElsnerCEO | | | |
|  | | | |
|  |  |  |  |
| |  |  |  |  | | --- | --- | --- | --- | | Anna FaliCMO | | | | |  | | | | |  |  |  |  | | |  | | --- | | Sales | |  | | | | | |  | | --- | | Marketing | |  | | | | | | | |  |  |  |  | | --- | --- | --- | --- | | Stephen ShawCTO | | | | |  | | | | |  |  |  |  | | |  | | --- | | Development | |  | | | | | |  | | --- | | UI/UX Design | |  | | | | | | |

```

<OrganizationChart :value="data" collapsible>
    <template #person="slotProps">
        <div class="flex flex-col">
            <div class="flex flex-col items-center">
                <img :alt="slotProps.node.data.name" :src="slotProps.node.data.image" class="mb-4 w-12 h-12" />
                <span class="font-bold mb-2">{{ slotProps.node.data.name }}</span>
                <span>{{ slotProps.node.data.title }}</span>
            </div>
        </div>
    </template>
    <template #default="slotProps">
        <span>{{ slotProps.node.label }}</span>
    </template>
</OrganizationChart>


```

## Accessibility [#](https://primevue.org/organizationchart/#accessibility)

### Screen Reader

Component currently uses a table based implementation and does not provide high level of screen reader support, a nested list implementation replacement is planned with aria roles and attributes aligned to a tree widget for high level of reader support in the upcoming versions.

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus through the focusable elements within the chart. |
| *enter* | Toggles the expanded state of a node. |
| *space* | Toggles the expanded state of a node. |