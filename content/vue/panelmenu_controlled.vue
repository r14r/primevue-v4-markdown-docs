<Button type="button" label="Toggle All" text @click="toggleAll" />
<PanelMenu v-model:expandedKeys="expandedKeys" :model="items" />