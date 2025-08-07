# IftaLabel

IftaLabel is used to create infield top aligned labels

## Import [#](https://primevue.org/iftalabel/#import)

```

import IftaLabel from 'primevue/iftalabel';


```

## Basic [#](https://primevue.org/iftalabel/#basic)

IftaLabel is used by wrapping the input and its label.

Username

```

<IftaLabel>
    <InputText id="username" v-model="value" />
    <label for="username">Username</label>
</IftaLabel>


```

## Invalid [#](https://primevue.org/iftalabel/#invalid)

When the form element is invalid, the label is also highlighted.

Username

```

<IftaLabel>
    <InputText id="username" v-model="value" :invalid="!value" />
    <label for="username">Username</label>
</IftaLabel>


```

## Accessibility [#](https://primevue.org/iftalabel/#accessibility)

### Screen Reader

IftaLabel does not require any roles and attributes.

### Keyboard Support

Component does not include any interactive elements.