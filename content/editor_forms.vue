<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col gap-1">
        <Editor name="content" editorStyle="height: 320px" />
        <Message v-if="$form.content?.invalid" severity="error" size="small" variant="simple">{{ $form.content.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>