(function () {
  const api = window.ABTest || {};
  const staatusElement = document.getElementById("api-staatus");
  const tulemusedElement = document.getElementById("api-tulemused");
  const konteiner = document.getElementById("variant-container");
  const toggleNupp = document.getElementById("variant-toggle");
  const valikuSilt = document.getElementById("valiku-label");

  if (!konteiner || !toggleNupp) return;

  const taastatud = api.taastaVariant ? api.taastaVariant() : null;
  let aktiivne = api.valiVariant
    ? api.valiVariant(taastatud)
    : { variant: "variant_a", sessioonId: "sess-unknown" };

  function saadaGaSyndmus(nimi, lisa = {}) {
    if (typeof window.gtag !== "function") return;

    const baas = api.looSyndmuseKeha
      ? api.looSyndmuseKeha(
          lisa.variant || aktiivne.variant,
          lisa.katsestaadium || "vaade",
          lisa
        )
      : lisa;

    window.gtag("event", nimi, {
      ...baas,
      sessioonId: aktiivne.sessioonId,
      timestamp: new Date().toISOString(),
    });
  }

  function kuvaVariant() {
    konteiner.innerHTML = api.looLayoutHTML(aktiivne.variant);
    valikuSilt.textContent = `Aktiivne: ${aktiivne.variant}`;
    api.salvestaVariant(aktiivne.variant);

    // ⬅ GA: variant_vaade
    saadaGaSyndmus("variant_vaade", {
      variant: aktiivne.variant,
      katsestaadium: "variant_vaade",
    });
  }

  async function laeKoondAndmed() {
    if (!staatusElement || !tulemusedElement) return;

    staatusElement.textContent = "Laen andmeid…";
    staatusElement.classList.remove("viga");

    try {
      const vastus = await fetch(window.API_URL);
      if (!vastus.ok) throw new Error(`Vigane staatus ${vastus.status}`);

      const keha = await vastus.json();
      tulemusedElement.textContent = JSON.stringify(keha, null, 2);
      staatusElement.textContent = "Andmed laetud";
    } catch (err) {
      staatusElement.textContent = "Viga andmete laadimisel";
      staatusElement.classList.add("viga");

      saadaGaSyndmus("variant_viga", {
        variant: aktiivne.variant,
        pohjus: err.message,
      });

      tulemusedElement.textContent = String(err);
    }
  }

  toggleNupp.addEventListener("click", () => {
    const vana = aktiivne.variant;
    aktiivne.variant = api.vahetaVariant(aktiivne.variant);

    kuvaVariant();

    // ⬅ GA: variant_vahetus
    saadaGaSyndmus("variant_vahetus", {
      previous_variant: vana,
      new_variant: aktiivne.variant,
      katsestaadium: "variant_vahetus",
    });
  });

  kuvaVariant();
  laeKoondAndmed();
})();
