(function () {
  const api = window.ABTest || {};
  const variantVoimalik = api.VARIANDID || [];
  const staatusElement = document.getElementById("api-staatus");
  const tulemusedElement = document.getElementById("api-tulemused");
  const konteiner = document.getElementById("variant-container");
  const toggleNupp = document.getElementById("variant-toggle");
  const valikuSilt = document.getElementById("valiku-label");

  if (!konteiner || !toggleNupp) {
    return;
  }

  const taastatud = api.taastaVariant ? api.taastaVariant() : null;
  let aktiivne = api.valiVariant
    ? api.valiVariant(taastatud)
    : { variant: variantVoimalik[0], sessioonId: "sess-unknown" };

  function kuvaVariant() {
    if (!api.looLayoutHTML) return;
    konteiner.innerHTML = api.looLayoutHTML(aktiivne.variant);
    valikuSilt.textContent = `Aktiivne: ${aktiivne.variant}`;
    if (api.salvestaVariant) {
      api.salvestaVariant(aktiivne.variant);
    }
    saadaGaSyndmus("variant_vaade", { variant: aktiivne.variant });
  }

  async function laeKoondAndmed() {
    if (!staatusElement || !tulemusedElement) {
      return;
    }
    staatusElement.textContent = "Laen andmeid…";
    staatusElement.classList.remove("viga");
    try {
      const vastus = await fetch(window.API_URL);
      if (!vastus.ok) {
        throw new Error(`Vigane staatus ${vastus.status}`);
      }
      const keha = await vastus.json();
      tulemusedElement.textContent = JSON.stringify(keha, null, 2);
      staatusElement.textContent = "Andmed laetud";
    } catch (err) {
      staatusElement.textContent = "Viga andmete laadimisel";
      staatusElement.classList.add("viga");
      tulemusedElement.textContent = String(err);
      saadaGaSyndmus("variant_viga", {
        variant: aktiivne.variant,
        pohjus: err.message,
      });
    }
  }

  function saadaGaSyndmus(nimi, lisa = {}) {
    if (typeof window.gtag !== "function") {
      return;
    }
    const baas = api.looSyndmuseKeha
      ? api.looSyndmuseKeha(
          lisa.variant || aktiivne.variant,
          lisa.katsestaadium || "esileht",
          lisa
        )
      : lisa;
      console.log("GA Event:", nimi, baas);
    window.gtag("event", nimi, {
      ...baas,
      sessioonId: aktiivne.sessioonId,
      timestamp: new Date().toISOString(),
    });
  }

  toggleNupp.addEventListener("click", () => {
    aktiivne = {
      variant: api.vahetaVariant
        ? api.vahetaVariant(aktiivne.variant)
        : aktiivne.variant,
      sessioonId: aktiivne.sessioonId,
    };
    kuvaVariant();
    saadaGaSyndmus("variant_vahetus", { variant: aktiivne.variant });
  });

  kuvaVariant();
  laeKoondAndmed();
})();

