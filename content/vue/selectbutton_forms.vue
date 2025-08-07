<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col gap-1">
        <SelectButton name="selection" :options="options" />
        <Message v-if="$form.selection?.invalid" severity="error">{{ $form.selection.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>