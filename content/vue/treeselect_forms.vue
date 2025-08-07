<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-full md:w-80">
    <div class="flex flex-col gap-1">
        <TreeSelect name="node" :options="nodes" placeholder="Select Item" fluid />
        <Message v-if="$form.node?.invalid" severity="error" size="small" variant="simple">{{ $form.node.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>