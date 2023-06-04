<script>
  import "../../app.postcss";
  import { page } from "$app/stores";
  import "../styles.css";
</script>

<div class="w-full">
  <div class="mx-auto flex mb-20 flex-col container">
    <slot />
  </div>
</div>
