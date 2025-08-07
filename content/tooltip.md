# Tooltip

Tooltip directive provides advisory information for a component.

## Import [#](https://primevue.org/tooltip/#import)

```

import Tooltip from 'primevue/tooltip';

app.directive('tooltip', Tooltip);


```

## Position [#](https://primevue.org/tooltip/#position)

There are four choices to position the tooltip, default value is *right* and alternatives are *top*, *bottom*, *left*.

```

<InputText v-tooltip="'Enter your username'" type="text" placeholder="Right" />
<InputText v-tooltip.top="'Enter your username'" type="text" placeholder="Top" />
<InputText v-tooltip.bottom="'Enter your username'" type="text" placeholder="Bottom" />
<InputText v-tooltip.left="'Enter your username'" type="text" placeholder="Left" />


```

## Event [#](https://primevue.org/tooltip/#event)

Event to display the tooltip is defined as a modifier, default event is hover.

```

<InputText v-tooltip.focus.top="'Enter your username'" type="text" placeholder="Focus" />


```

## Auto Hide [#](https://primevue.org/tooltip/#autohide)

Tooltip gets hidden when mouse leaves the target element by default, set *autoHide* to false to customize this behavior so that tooltip stays open when the cursor is on the tooltip.

```

<InputText v-tooltip.bottom="{ value: 'Enter your username', autoHide: false }" type="text" placeholder="autoHide: false" />
<InputText v-tooltip.bottom="'Enter your username'" type="text" placeholder="autoHide: true" />


```

## Delay [#](https://primevue.org/tooltip/#delay)

Delays to the enter and leave events are defined with *showDelay* and *hideDelay* options respectively.

Save

```

<Button v-tooltip="{ value: 'Confirm to proceed', showDelay: 1000, hideDelay: 300 }" label="Save" />


```

## Custom [#](https://primevue.org/tooltip/#custom)

A tooltip sample with a custom style and content.

Button

```

<Button
    v-tooltip.bottom="{
        value: 'PrimeVue Rocks',
        pt: {
            arrow: {
                style: {
                    borderBottomColor: 'var(--p-primary-color)'
                }
            },
            text: '!bg-primary !text-primary-contrast !font-medium'
        }
    }"
    label="Button"
/>


```

## Accessibility [#](https://primevue.org/tooltip/#accessibility)

### Screen Reader

Tooltip component uses *tooltip* role and when it becomes visible the generated id of the tooltip is defined as the *aria-describedby* of the target.

### Keyboard Support

| Key | Function |
| --- | --- |
| *escape* | Closes the tooltip when focus is on the target. |