# Editor

Editor is rich text editor component based on Quill.

## Import [#](https://primevue.org/editor/#import)

```

import Editor from 'primevue/editor';


```

## Quill [#](https://primevue.org/editor/#quill)

Editor uses [Quill](https://quilljs.com/) editor underneath so it needs to be installed as a dependency.

```

npm install quill


```

## Basic [#](https://primevue.org/editor/#basic)

Editor is used with the *v-model* property for two-way value binding.

HeadingSubheadingNormal

```

<Editor v-model="value" editorStyle="height: 320px" />


```

## Forms [#](https://primevue.org/editor/#forms)

Editor integrates seamlessly with the [PrimeVue Forms](https://primevue.org/forms) library.

HeadingSubheadingNormal

Submit

```

<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col gap-1">
        <Editor name="content" editorStyle="height: 320px" />
        <Message v-if="$form.content?.invalid" severity="error" size="small" variant="simple">{{ $form.content.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>


```

## ReadOnly [#](https://primevue.org/editor/#readonly)

When *readonly* is present, the value cannot be edited.

HeadingSubheadingNormal

```

<Editor v-model="value" editorStyle="height: 320px" readonly />


```

## Template [#](https://primevue.org/editor/#template)

Editor provides a default toolbar with common options, to customize it define your elements inside the header element. Refer to [Quill documentation](http://quilljs.com/docs/modules/toolbar/) for available controls.

```

<Editor v-model="value" editorStyle="height: 320px">
    <template v-slot:toolbar>
        <span class="ql-formats">
            <button v-tooltip.bottom="'Bold'" class="ql-bold"></button>
            <button v-tooltip.bottom="'Italic'" class="ql-italic"></button>
            <button v-tooltip.bottom="'Underline'" class="ql-underline"></button>
        </span>
    </template>
</Editor>


```

## Accessibility [#](https://primevue.org/editor/#accessibility)

### Screen Reader

Quill performs generally well in terms of accessibility. The elements in the toolbar can be tabbed and have the necessary ARIA roles/attributes for screen readers. One known limitation is the lack of arrow key support for [dropdowns](https://github.com/quilljs/quill/issues/1031) in the toolbar that may be overcome with a custom toolbar.